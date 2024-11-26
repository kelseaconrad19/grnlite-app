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

  &:disabled {
    background-color: #95a5a6;
    cursor: not-allowed;
  }
`;

const SecondarySignUp = () => {
  const { role } = useParams(); // Get role (Author, Reader, Editor) from URL
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    preferences: '',
    genres: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const validateForm = () => {
    if (!formData.name || !formData.email || !formData.password || !formData.preferences) {
      setError('All fields are required!');
      return false;
    }
    setError('');
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsSubmitting(true);

    try {
      // Replace this with an actual API call
      const response = await fakeApiCall(formData);
      
      if (response.success) {
        alert('Your account has been created!');
        // Navigate to another page or reset the form
      } else {
        setError('There was an issue with your signup.');
      }
    } catch (err) {
      setError('An error occurred. Please try again later.');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Simulating an API call
  const fakeApiCall = (data) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        if (data.email !== 'fail@example.com') {
          resolve({ success: true });
        } else {
          resolve({ success: false });
        }
      }, 2000);
    });
  };

  return (
    <Container>
      <h1>Sign Up as {role.charAt(0).toUpperCase() + role.slice(1)}</h1>
      <Form onSubmit={handleSubmit}>
        {error && <p style={{ color: 'red' }}>{error}</p>}
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
        {role === 'editor' && (
          <>
            <Input
              type="text"
              name="preferences"
              placeholder="Specialization (e.g., Grammar, Developmental Editing)"
              value={formData.preferences}
              onChange={handleChange}
              required
            />
            <Select
              name="genres"
              value={formData.genres}
              onChange={handleChange}
              required
            >
              <option value="" disabled>
                Select Genres You Edit
              </option>
              <option value="fiction">Fiction</option>
              <option value="non-fiction">Non-Fiction</option>
              <option value="fantasy">Fantasy</option>
              <option value="biography">Biography</option>
            </Select>
          </>
        )}
        <Button type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Signing Up...' : 'Sign Up'}
        </Button>
      </Form>
    </Container>
  );
};

export default SecondarySignUp;
