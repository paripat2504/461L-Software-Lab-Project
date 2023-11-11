import React from 'react';
import { useState } from 'react'; 
import { useNavigate } from "react-router";
import Modal from 'react-modal';
import { useAuth } from './UserContext';

function JoinProject({fetchProjects, isOpen, onRequestClose}) {
    const navigate = useNavigate();
    const { userName } = useAuth();
    const [id, setID] = useState('');
    const [message, setMessage] = useState('');

    const handleConfirm = async (e) => {
        e.preventDefault();
        if(id === '') {
            setMessage("Please fill out all fields");
            return;
        }

        try {
            const response = await fetch('https://mejiasoftwareproject-ba462176bcee.herokuapp.com/projectJoin', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({ userName:userName, projectID:id })
            });
          
            const data = await response.json();
            //Handle message
            alert(data.message);
            if(data.message === 'Project Joined successfully'){
                onRequestClose();
                setID('');
                setMessage('');
                fetchProjects();
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
                <h1 className="font-bold text-center block text-3xl">Join an existing project</h1>
                <div>
                    <label className="text-gray-500 block mt-3">Project ID</label>
                    <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                    placeholder='ID of the project you want to join'
                    style={{marginRight:'10px'}}
                    value={id}
                    onChange={handleID}
                    />
                </div>
                <div className="text-red-600 flex justify-center">{message}</div>
                <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg" onClick={(e) => handleConfirm(e)}>Confirm</button>
            </form>
            </div>
        </Modal>
    );
}

export default JoinProject;
