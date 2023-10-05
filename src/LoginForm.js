import { useState } from 'react'; 
import { useNavigate } from "react-router";


function LoginForm() {
    const navigate = useNavigate();
    //PLACEHOLDER UNTIL WE SEND ACTUAL HTTP REQUESTS TO BACKEND
    const dummyDatabase = new Map();
    dummyDatabase.set('samant', 'SE-god');

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
  
    const handleUsername = (e) => {
      setUsername(e.target.value); 
    }
  
    const handlePassword = (e) => {
      setPassword(e.target.value); 
    }
  
    const handleClick = (e) => {
        e.preventDefault();
        //PLACEHOLDER LOGIC
        if (dummyDatabase.has(username)) {
            console.log(`Username '${username}' exists with value '${dummyDatabase.get(username)}'`);
          } else {
            console.log(`Access denied`);
          }
    };

    const handleSignup = () => {
        console.log("User wants to sign up.")
    }
  
  
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
          <button type="button" onClick={() => {navigate('/signup')}}>Sign up</button>
    </form>
    );
  }
  
  export default LoginForm;