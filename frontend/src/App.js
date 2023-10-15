import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {NormalizeStyles} from './shared/NormalizeStyles';
import {Home} from './screens/Home';

function App() {
  return (
    <>
    <NormalizeStyles />
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
