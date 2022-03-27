import React, { useState } from "react";
import './Home.scss';
import { Button } from 'react-bootstrap'

const Home = () => {
    
    const [count, setCount] = useState(0);
    return (
        <h1 className="d-">
            <Button onClick={() => {
                setCount(count+1);
            }}> Here</Button>
            <div>{count}</div>
        </h1>
    )
}

export default Home;