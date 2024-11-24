import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import HeroSection from './components/HeroSection';
import Features from './components/Features';
import AboutUs from './components/AboutUs';
import ContactForm from './components/ContactForm';
import Footer from './components/Footer';
import SignIn from './pages/SignIn';
import SecondarySignIn from './pages/SecondarySignIn';
import SignUp from './pages/SignUp'; 
import SecondarySignUp from './pages/SecondarySignUp';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route
            path="/"
            element={
              <>
                <HeroSection />
                <Features />
                <AboutUs />
                <ContactForm />
              </>
            }
          />
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-in/:role" element={<SecondarySignIn />} />
          <Route path="/sign-up" element={<SignUp />} /> 
          <Route path="/sign-up/:role" element={<SecondarySignUp />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
