import logo from './logo.svg';
// import './App.css';
import LoginForm from './LoginForm';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUpForm from './SignUpForm';
import HomePage from './homePage';
import AddProject from './AddProject';

function App() {
  return (
    <Router>
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/signup" element={<SignUpForm/>} />
          <Route path="/home" element={<HomePage/>} />
          <Route path="/addproject" element={<AddProject/>} />
        </Routes>
      </header>
    </div>
    </Router>
    
  );
}

export default App;
