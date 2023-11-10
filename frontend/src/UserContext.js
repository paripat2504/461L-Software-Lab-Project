import { createContext, useState, useContext, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [userId, setUserId] = useState(() => {
        return localStorage.getItem('userId') || null;
    });

    const [userName, setUserName] = useState(() => {
        return localStorage.getItem('userName') || null;
    });
    //Maybe for future use if we want to incorporate tokens for authentication
    const [token, setToken] = useState(null); 

    const login = (userId, userName) => {
        setUserId(userId, userName);
        setUserName(userName);
        localStorage.setItem('userId', userId);
        localStorage.setItem('userName', userName);
    }

    const logout = () => {
        setUserId(null);
        setUserName(null);
        localStorage.removeItem('userId');
        localStorage.removeItem('userName');
    }

    return (
        <AuthContext.Provider value={{userId, userName, login, logout}}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => {return useContext(AuthContext)};