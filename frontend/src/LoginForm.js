import { useState } from 'react'; 
import { useNavigate } from "react-router";

function LoginForm() {
    const navigate = useNavigate();

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
  
    const handleUsername = (e) => {
      setUsername(e.target.value); 
    }
  
    const handlePassword = (e) => {
      setPassword(e.target.value); 
    }
  
    const handleClick = async (e) => {
        e.preventDefault();
        try {
          const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userID: username, password })
          });
        
          const data = await response.json();
          //Handle message
          setMessage(data.message);
        } catch (err) {
          console.error(err);
          setMessage("An error occured: " + err)
        };
    };

    const handleSignupClick = () => {
      navigate('/signup');
    };
  
    return (
      <form onSubmit={handleClick}>
        <h1>Login Page</h1>
          <div>
            <label>User ID</label>
            <input type="text"
              placeholder='Enter your username'
              style={{marginRight:'10px'}}
              value={username}
              onChange={handleUsername}
            />
          </div>
          <div>
            <label>Password</label>
            <input type="password"
              placeholder='Enter your password'
              value={password}
              onChange={handlePassword}  
            />
          </div>
          <button type="submit" onClick={handleClick} style={{marginRight:'20px'}}>Login</button>
          <button type="button" onClick={handleSignupClick}>Sign up</button>
          <div>{message}</div>
    </form>
    );
  }
  
  export default LoginForm;