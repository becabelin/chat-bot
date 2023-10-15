import styled from 'styled-components';

export const ChatContainer = styled.div`
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 300px;
  border: 1px solid #007bff;
  border-radius: 10px;
  background-color: #f7f7f7;
  display: flex;
  flex-direction: column;
`;

export const MessageContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin: 10px;
`;

export const UserMessage = styled.div`
  background: #007bff;
  color: #fff;
  border-radius: 10px;
  padding: 8px;
  margin: 5px 0;
`;

export const BotMessage = styled.div`
  background: #eee;
  border-radius: 10px;
  padding: 8px;
  margin: 5px 0;
`;

export const Form = styled.form`
  display: flex;
  margin: 10px;
`;

export const Input = styled.input`
  flex: 1;
  border: none;
  border-radius: 10px;
  padding: 10px;
  margin-right: 10px;
  font-size: 16px;
`;

export const SendButton = styled.button`
  background: #007bff;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
`;
