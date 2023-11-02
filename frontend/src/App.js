import logo from './logo.svg';
// import './App.css';
import LoginForm from './LoginForm';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUpForm from './SignUpForm';


function App() {
  return (
    <Router>
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/signup" element={<SignUpForm/>} />
        </Routes>
      </header>
    </div>
    </Router>
  );
}

export default App;
