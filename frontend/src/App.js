import React, { useState } from 'react';
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
import AuthorDashboard from './pages/AuthorDashboard'; 
import ReaderDashboard from './pages/ReaderDashboard';
import ProtectedRoute from './components/ProtectedRoute'; 
import './App.css';

function App() {
  const [user, setUser] = useState(null); // State to store logged-in user details

  const isAuthenticated = user !== null; // Check if user is logged in
  const isAuthor = user?.role === 'author'; // Check if user is an author
  const isReader = user?.role === 'reader'; // Check if user is a reader
  const isEditor = user?.role === 'editor'; // Check if user is an editor

  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          {/* Home Page */}
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

          {/* Sign-In Pages */}
          <Route path="/sign-in" element={<SignIn setUser={setUser} />} />
          <Route path="/sign-in/:role" element={<SecondarySignIn setUser={setUser} />} />

          {/* Sign-Up Pages */}
          <Route path="/sign-up" element={<SignUp setUser={setUser} />} />
          <Route path="/sign-up/:role" element={<SecondarySignUp setUser={setUser} />} />

          {/* Protected Author Dashboard */}
          <Route
            path="/author-dashboard"
            element={
              <ProtectedRoute isAuthenticated={isAuthenticated && isAuthor}>
                <AuthorDashboard />
              </ProtectedRoute>
            }
          />

          {/* Protected Reader Dashboard */}
          <Route
            path="/reader-dashboard"
            element={
              <ProtectedRoute isAuthenticated={isAuthenticated && isReader}>
                <ReaderDashboard />
              </ProtectedRoute>
            }
          />

          {/* Future Editor Dashboard */}
          {isEditor && (
            <Route
              path="/editor-dashboard"
              element={
                <ProtectedRoute isAuthenticated={isAuthenticated && isEditor}>
                  {/* Add your EditorDashboard component here */}
                  <div>Editor Dashboard - Coming Soon!</div>
                </ProtectedRoute>
              }
            />
          )}
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
