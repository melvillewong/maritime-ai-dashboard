// src/main.tsx (or src/index.tsx)
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';  // Optional, you can leave this out if you don't have custom styles yet

const root = document.getElementById('root') as HTMLElement;
ReactDOM.createRoot(root).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
