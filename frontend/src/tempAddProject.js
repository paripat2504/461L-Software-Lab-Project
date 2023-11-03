import React from 'react';
import { useState } from 'react'; 
import { useNavigate } from "react-router";



function AddProject() {
    const navigate = useNavigate();
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [id, setID] = useState('');

    const handleName = (e) => {
        setName(e.target.value)
    }

    const handleDescription = (e) => {
        setDescription(e.target.value)
    }


    const handleConfirm = (e) => {
        e.preventDefault();
        // if(name === '' || description === '' || id === '') {
        //     setMessage("Please fill out all fields");
        //     return;
        // }

        // DO FETCH TO ADD PROJECT ENDPOINT

        //reroute to homepage
        navigate('/home');
    }

    const handleClick = (e) => {
        e.preventDefault();
    }

    const handleID = (e) => {
        setID(e.target.value)
    }

    return (
        <div className="flex justify-center items-center h-screen w-screen">
        <div className=" border-t-8 rounded-md border-amber-600 bg-white p-14 shadow-2xl w-96">
        <form onSubmit={handleClick}>
            <h1 className="font-bold text-center block text-3xl">Create new project</h1>
            <div>
                <label className="text-gray-500 block mt-3">Name</label>
                <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                placeholder='Enter a name for your project'
                style={{marginRight:'10px'}}
                value={name}
                onChange={handleName}
                />
            </div>
            <div>
                <label className="text-gray-500 block mt-3">Description</label>
                <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="password"
                placeholder='Enter a description for your project'
                value={description}
                onChange={handleDescription}  
                />
            </div>
            <div>
                <label className="text-gray-500 block mt-3">Project ID</label>
                <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="password"
                placeholder='Enter a Project ID'
                value={id}
                onChange={handleID}  
                />
            </div>
            {/* <div className="text-red-600 flex justify-center">{message}</div> */}
            <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={handleConfirm}>Confirm</button>
            
        </form>
        </div>
        </div>
    );
}

export default AddProject;
