import { useState } from 'react';
import { useNavigate } from "react-router";
function SignUpForm() {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [userID, setUserID] = useState('');
  const [password, setPassword] = useState('');
  const [secondPassword, setSecondPassword] = useState('');


  const handleUsername = (e) => {
    setUsername(e.target.value); 
  }

  const handlePassword = (e) => {
    setPassword(e.target.value); 
  }

  const handleSecondPassword = (e) => {
    setSecondPassword(e.target.value); 
  }

  const handleUserID = (e) => {
    setUserID(e.target.value); 
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if(password !== secondPassword) {
      alert("Entered passwords do not match");
      return;
    }

    if(username === '' || password === '' || userID === '' || secondPassword === '') {
      alert("All fields were not filled out");
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
          body: JSON.stringify({ userName:username, password:password, userID:userID })
      });

      const data = await response.json();
      console.log(data.message);

      if (data.message === "User registered successfully") {
          alert("User registered successfully")
          navigate('/');
      } else if (data.message === "User already exists") {
          alert("User already exists");
      } else {
          alert("An error occured: " + data.message);
      }
    } catch (err) {
      console.error(err);
    }
  };

    return (
    <div className="SignUpForm">
      <header className="SignUpForm-header">
        <h1>Sign Up</h1>
          <div>
            <label>User ID</label>
            <input type="text"
              placeholder='Enter your User ID'
              style={{marginRight:'10px'}}
              value={userID}
              onChange={handleUserID}
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
              value={secondPassword}
              onChange={handleSecondPassword}
            />
          </div>
          <button type="submit" onClick={() => {navigate('/')}} style={{marginRight:'20px'}}>Back</button>
          <button type="submit" onClick={handleSubmit} style={{marginRight:'20px'}}>Submit</button>
      </header>
    </div>
    );
};

export default SignUpForm;