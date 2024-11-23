import React from 'react';
import styled from 'styled-components';

const FooterContainer = styled.footer`
  padding: 20px;
  background-color: #145a32;
  color: white;
  text-align: center;
`;

const Footer = () => (
  <FooterContainer>
    <p>&copy; 2024 Grn Lite. All Rights Reserved.</p>
  </FooterContainer>
);

export default Footer;
