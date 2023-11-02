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
            body: JSON.stringify({ userID:username, password })
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
      <div className="bg-blue-70 flex justify-center items-center h-screen w-screen">
      <div className=" border-t-8 rounded-sm border-indigo-600 bg-white p-12 shadow-2xl w-96">
      <form onSubmit={handleClick}>
        <h1 className="font-italic text-center block text-2xl">Login Page</h1>
          <div>
            <label className="text-gray-500 block mt-3">User ID</label>
            <input type="text"
              placeholder='Enter your User ID'
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
          <button type="submit" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg" onClick={handleClick} style={{marginRight:'20px'}}>Login</button>
          <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={handleSignupClick}>Sign up</button>
          <div>{message}</div>
    </form>
    </div>
    </div>
    );
  }
  
  export default LoginForm;