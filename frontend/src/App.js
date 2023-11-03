import logo from './logo.svg';
// import './App.css';
import LoginForm from './LoginForm';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUpForm from './SignUpForm';
import HomePage from './homePage';


function App() {
  return (
    <Router>
    <div className="App bg-gray-100">
      <header className="App-header">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/signup" element={<SignUpForm/>} />
          <Route path="/home" element={<HomePage/>} />
        </Routes>
      </header>
    </div>
    </Router>
    
  );
}

export default App;
