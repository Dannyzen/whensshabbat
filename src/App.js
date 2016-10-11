import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Form from './Form';

class App extends Component {


    render() {
        return (
            <div className="App"
                 style={{height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <Form/>
            </div>
        );
    }
}

export default App;
