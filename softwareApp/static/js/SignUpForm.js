import { useState } from 'react';
import { useNavigate } from "react-router";
import { useLocation } from 'react-router-dom';

function SignUpForm() {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const location = useLocation();
  const { dummyDatabase } = location.state;

  const handleUsername = (e) => {
    setUsername(e.target.value); 
  }

  const handlePassword = (e) => {
    setPassword(e.target.value); 
  }

  const handleSubmit = () => {
    dummyDatabase.set(username, password);
    navigate('/');
  };

    return (
    <div className="SignUpForm">
      <header className="SignUpForm-header">
        <h1>Sign Up</h1>
          <div>
            <label>Full Name</label>
            <input type="text"
              placeholder='Enter your full name'
              style={{marginRight:'10px'}}
            />
          </div>
          <div>
            <label>Username</label>
            <input type="text"
              placeholder='Enter your desired username'
              value={username}
              onChange={handleUsername}
            />
          </div>
          <div>
            <label>Password</label>
            <input type="password"
              placeholder='Enter your desired password'
              value={password}
              onChange={handlePassword} 
            />
          </div>
          <div>
          <label>Re-enter Password</label>
            <input type="password"
              placeholder='Enter password again'
            />
          </div>
          <div>
            <label>E-mail</label>
            <input type="email"
              placeholder='Enter your e-mail addresss'
            />
          </div>
          <button type="submit" onClick={() => {navigate('/')}} style={{marginRight:'20px'}}>Back</button>
          <button type="submit" onClick={handleSubmit} style={{marginRight:'20px'}}>Submit</button>
      </header>
    </div>
    );
};

export default SignUpForm;