import React from 'react';
import { BrowserRouter as Router, Routes, Route } from   'react-router-dom';

import Home from './pages/home.jsx';
import Plant1 from './pages/plant1.jsx';
import Plant2 from './pages/plant2.jsx';

function App(){
    return(
        <Router>
            <Routes>
                <Route path="/" element={<Home  />} />
                <Route path="/Plant1" element={<Plant1 />} />
                <Route path="/Plant2" element={<Plant2 />} />
            </Routes>
        </Router>
    )
}

export default App;