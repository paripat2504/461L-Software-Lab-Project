import React from 'react';
import { useState } from 'react'; 
import { useNavigate } from "react-router";
import Modal from 'react-modal';
import { useAuth } from './UserContext';

function AddProject({isOpen, onRequestClose}) {
    const { userName } = useAuth();
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [id, setID] = useState('');
    const [message, setMessage] = useState('');

    const handleName = (e) => {
        setName(e.target.value)
    }

    const handleDescription = (e) => {
        setDescription(e.target.value)
    }

    const handleConfirm = async (e) => {
        e.preventDefault();
        if(name === '' || description === '' || id === '') {
            setMessage("Please fill out all fields");
            return;
        }

        try {
            const response = await fetch('http://localhost:5000/project', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({ userName:userName, projectName:name, projectDescription:description, projectID:id })
            });
          
            const data = await response.json();
            //Handle message
            alert(data.message);
            if(data.message === 'Project Created successfully'){
                onRequestClose();
                setName('');
                setDescription('');
                setID('');
                setMessage('');
            }
          } catch (err) {                                      
            console.error(err);
            alert("An error occured: " + err)
            onRequestClose();
          };


    }

    const handleID = (e) => {
        setID(e.target.value)
    }

    return (
        <Modal 
            isOpen={isOpen}
            onRequestClose={onRequestClose}
            className="justify-center overflow-x-hidden overflow-y-auto fixed items-center flex inset-0 z-50 outline-none focus:outline-none bg-gray-600 bg-opacity-75"
            ariaHideApp={false}
        >   
            <div className="border-t-8 rounded-md border-amber-600 bg-white p-14 shadow-2xl w-96 border-0 rounded-lg shadow-lg relative flex flex-col outline-none focus:outline-none">
            <button
                className="text-black h-6 w-6 text-4xl block outline-none focus:outline-none absolute top-1 right-5"
                onClick={onRequestClose}
            >×</button>
            <form onSubmit={handleConfirm}>
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
                    <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                    placeholder='Enter a description for your project'
                    value={description}
                    onChange={handleDescription}  
                    />
                </div>
                <div>
                    <label className="text-gray-500 block mt-3">Project ID</label>
                    <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                    placeholder='Enter a Project ID'
                    value={id}
                    onChange={handleID}  
                    />
                </div>
                <div className="text-red-600 flex justify-center">{message}</div>
                <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={(e) => handleConfirm(e)}>Confirm</button>
            </form>
            </div>
        </Modal>
    );
}

export default AddProject;
