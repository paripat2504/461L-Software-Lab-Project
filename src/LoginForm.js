import { useState } from 'react'; 
import './App.css'

function LoginForm() {
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
        console.log('Username entered:', username);
        console.log('Password entered:', password);
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
          <button onClick={handleClick}>Login</button>
          <button>Sign up</button>
    </form>
    );
  }
  
  export default LoginForm;