import React, { useState, useEffect } from 'react';
import {ChatContainer, MessageContainer, UserMessage, BotMessage,Form, Input, SendButton} from './styles'
import { useFormik } from "formik";
import * as Yup from "yup";
import axios from "axios";

export function ChatBot() {
  const [messages, setMessages] = useState([]);
  
  const Schema = Yup.object().shape({
    text: Yup.string().required("Campo obrigatório"),
  });
  
  const formik = useFormik({
    initialValues: {
      text: "",
    },
    onSubmit: (values) => {
      setMessages((currentState) => ( [...currentState, {text: values.text, type: 'user', action: ''}] ));
      formik.resetForm();

      const selectedOption = messages.find((message) => message.valor === values.text);
      if (selectedOption !== undefined) {
        getChatBotInfo(selectedOption.action);
      } else {
        setMessages((currentState) => ( [...currentState, {text: 'Insira uma opção válida', type: 'bot', action: ''}] ));
      }
    },
    validationSchema: Schema,
  });
  
  async function getChatBotInfo(path) {
    const response = await axios.get(`http://localhost:8000/${path}`);
    console.log(response.data)
    let messages = [{
      text: response.data.titulo,
      type: 'bot',
      action: '',
      valor: 0
    }];

    response.data.respostas.forEach((message) => {
      messages.push({
        text: `${message.valor} - ${message.descricao}`,
        type: 'bot',
        action: message.acao,
        valor: message.valor
      })
    });

    setMessages((currentState) => ( [...currentState, ...messages] ));
  }

  useEffect(() => {
    getChatBotInfo('api/v1/chatbot/principal')
  }, [])

  return (
    <ChatContainer>
      {messages.map((message, index) => (
        <MessageContainer key={index}>
          {message.type === 'user' ? (
            <UserMessage>{message.text}</UserMessage>
          ) : (
            <BotMessage>{message.text}</BotMessage>
          )}
        </MessageContainer>
      ))}
      <Form onSubmit={formik.handleSubmit}>
        <Input
            id='text'
            name='text'
            type="text"
            placeholder="Digite sua mensagem..."
            value={formik.values.text}
            onChange={formik.handleChange}
        />
        <SendButton type='submit'>Enviar</SendButton>
      </Form>
    </ChatContainer>
  );
};
