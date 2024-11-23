import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import HeroSection from './components/HeroSection';
import Features from './components/Features'; // Make sure to use this component
import AboutUs from './components/AboutUs'; // Make sure to use this component
import ContactForm from './components/ContactForm'; // Make sure to use this component
import Footer from './components/Footer';
import SignIn from './pages/SignIn';
import SecondarySignIn from './pages/SecondarySignIn';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={
            <>
              <HeroSection />
              <Features /> {/* Add the Features component */}
              <AboutUs /> {/* Add the About Us component */}
              <ContactForm /> {/* Add the ContactForm component */}
            </>
          } />
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-in/:role" element={<SecondarySignIn />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
