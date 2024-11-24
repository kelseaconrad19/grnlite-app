import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f4f4f4;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 400px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

const Input = styled.input`
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Select = styled.select`
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Button = styled.button`
  background-color: #27ae60;
  color: white;
  border: none;
  padding: 10px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #2ecc71;
  }
`;

const SecondarySignUp = () => {
  const { role } = useParams(); // Get role (Author or Reader) from URL
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    preferences: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Role: ${role}`, formData);
    alert('Your account has been created!');
    // Add backend integration here.
  };

  return (
    <Container>
      <h1>Sign Up as {role.charAt(0).toUpperCase() + role.slice(1)}</h1>
      <Form onSubmit={handleSubmit}>
        <Input
          type="text"
          name="name"
          placeholder="Full Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <Input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <Input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        {role === 'reader' && (
          <Select
            name="preferences"
            value={formData.preferences}
            onChange={handleChange}
            required
          >
            <option value="" disabled>
              Select Reading Preferences
            </option>
            <option value="fiction">Fiction</option>
            <option value="non-fiction">Non-Fiction</option>
            <option value="fantasy">Fantasy</option>
            <option value="science-fiction">Science Fiction</option>
          </Select>
        )}
        {role === 'author' && (
          <Input
            type="text"
            name="preferences"
            placeholder="Preferred Editing Style"
            value={formData.preferences}
            onChange={handleChange}
            required
          />
        )}
        <Button type="submit">Sign Up</Button>
      </Form>
    </Container>
  );
};

export default SecondarySignUp;
