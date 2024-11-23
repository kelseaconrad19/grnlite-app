import React from 'react';
import styled from 'styled-components';

const FeaturesContainer = styled.div`
  padding: 50px 20px;
  background-color: #f4f4f4;
  text-align: center;
`;

const FeatureCards = styled.div`
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
`;

const Card = styled.div`
  background: white;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

  &:hover {
    transform: translateY(-10px);
    transition: 0.3s ease;
  }
`;

const Features = () => (
  <FeaturesContainer id="features">
    <h2>Features</h2>
    <FeatureCards>
      <Card>
        <h3>Author Dashboards</h3>
        <p>Manage your manuscripts and connect with beta readers.</p>
      </Card>
      <Card>
        <h3>Beta Reader Profiles</h3>
        <p>Discover readers and view their feedback history.</p>
      </Card>
      <Card>
        <h3>Editor Portfolios</h3>
        <p>Find experienced editors for your manuscripts.</p>
      </Card>
    </FeatureCards>
  </FeaturesContainer>
);

export default Features;
