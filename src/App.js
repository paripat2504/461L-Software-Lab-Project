import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Login Page</h1>
        <div>
          <label>User ID</label>
          <input type="text" placeholder='Enter your username' style={{marginRight:'10px'}}/>
        </div>
        <div>
          <label>Password</label>
          <input type="text" placeholder='Enter your password'/>
        </div>
        <button>Login</button>
        <button>Sign up</button>
      </header>
    </div>
  );
}

export default App;
