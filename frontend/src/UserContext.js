import { createContext, useState, useContext, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [userId, setUserId] = useState(() => {
        return localStorage.getItem('userId') || null;
    });
    //Maybe for future use if we want to incorporate tokens for authentication
    const [token, setToken] = useState(null); 

    const login = (userId) => {
        setUserId(userId);
        localStorage.setItem('userId', userId);
    }

    const logout = () => {
        setUserId(null);
        localStorage.removeItem('userId');
    }

    return (
        <AuthContext.Provider value={{userId, login, logout}}>
            {children}
        </AuthContext.Provider>
    );
}

export const useAuth = () => {return useContext(AuthContext)};