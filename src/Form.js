import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import request from 'superagent';

class Holiday extends Component {

    render() {

        const {
            category,
            date,
            hebrew,
            link,
            memo,
            title
        } = this.props.item;

        return <div>{title}</div>;

    }
}

class Form extends Component {

    constructor(props) {
        super(props);
        this.state = {res: false};
    }

    send = ()=> {


        const zip = this._zipCode.value;


        request.get('https://www.hebcal.com/shabbat/').query({'cfg': 'json', 'm': 50, 'b': 18, 'zip': zip, 'a': 'on'})
            .end((err, res) => {
                if (err) {
                    // hsndle re
                }
                else {
                    this.setState({res: res.body});
                }
            });

    };

    refZipCode = c=>this._zipCode = c;

    render() {

        const {res} = this.state;

        console.log(res);

        return (
            <div>
                <h1>What time is Shabbat?</h1>
                <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                    <input type="text" ref={this.refZipCode} placeHolder="Zip code"/>
                    <button onClick={this.send}>Submit</button>
                </div>
                {res ? <Holiday item={res.items.filter(item=>item.category === 'candles')[0]}/> : false}
                {res ? <Holiday item={res.items.filter(item=>item.category === 'havdalah')[0]}/> : false}
            </div>
        );
    }
}

export default Form;
