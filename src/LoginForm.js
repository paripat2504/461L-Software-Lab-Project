import { useState } from 'react'; 
import { useNavigate } from "react-router";

function LoginForm() {
    const navigate = useNavigate();
    //PLACEHOLDER UNTIL WE CONNECT TO BACKEND
    const dummyDatabase = new Map();
    dummyDatabase.set('samant', 'SE-god');

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
  
    const handleUsername = (e) => {
      setUsername(e.target.value); 
    }
  
    const handlePassword = (e) => {
      setPassword(e.target.value); 
    }
  
    const handleClick = (e) => {
        e.preventDefault();
        //PLACEHOLDER LOGIC
        var msg = ''
        if (dummyDatabase.has(username)) {
            msg = `Username '${username}' exists with password '${dummyDatabase.get(username)}'`;
          } else {
            msg = `Access denied`;
          }
        setMessage(msg);
    };

    const handleSignupClick = () => {
      navigate('/signup', { state: { dummyDatabase } });
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