import React from 'react';
import styled from 'styled-components';

const ContactContainer = styled.div`
  padding: 50px 20px;
  text-align: center;
  background: #f4f4f4;
`;

const Form = styled.form`
  max-width: 400px;
  margin: 0 auto;
`;

const Input = styled.input`
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

const TextArea = styled.textarea`
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

const Button = styled.button`
  background-color: #27ae60;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #145a32;
  }
`;

const ContactForm = () => (
  <ContactContainer id="contact">
    <h2>Contact Us</h2>
    <Form>
      <Input type="text" placeholder="Your Name" />
      <Input type="email" placeholder="Your Email" />
      <TextArea rows="5" placeholder="Your Message"></TextArea>
      <Button type="submit">Send Message</Button>
    </Form>
  </ContactContainer>
);

export default ContactForm;
