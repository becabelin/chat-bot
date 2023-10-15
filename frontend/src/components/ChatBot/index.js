import React, { useState, useEffect } from 'react';
import {ChatContainer, MessageContainer, UserMessage, BotMessage,Form, Input, SendButton} from './styles'
import { useFormik } from "formik";
import * as Yup from "yup";


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
        console.log(values);
      setMessages((currentState) => ( [...currentState, {text: values.text, type: 'user'}] ));
      formik.resetForm();
    },
    validationSchema: Schema,
  });

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
