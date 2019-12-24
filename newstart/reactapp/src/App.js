import 'react-date-range/dist/styles.css'; // main style file
import 'react-date-range/dist/theme/default.css'; // theme css fileimport 'react-dates/initialize';
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import './App.css';
import { Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {ButtonToolbar} from 'react-bootstrap';
import {ButtonGroup} from 'react-bootstrap';
import {DropdownButton} from 'react-bootstrap';
import {Dropdown} from 'react-bootstrap';
import DateRangePicker from 'react-daterange-picker'
import 'react-daterange-picker/dist/css/react-calendar.css' // For some basic styling. (OPTIONAL)
function background() {
  return (
    <div
      style={{
        backgroundColor: 'blue',
        width: '100px',
        height: '100px'
      }}
    />
  );
}

class App extends Component {
shoot()
{
  ReactDOM.render(<DateComm />, document.getElementById('root'));

}

  render() {
    return (
      <div className="App">
      <div>
      <ButtonGroup vertical>
      <Button onClick={this.shoot}>Refine By Date Range and Commodity</Button>
      <Button>Refine By Date Range</Button>
      <Button>Refine By Commodity</Button>
      </ButtonGroup>
  </div>
      </div>
    )
  }
}

class Test extends React.Component {
  render() {
     return (
        <div
          style={{
            backgroundColor: 'blue',
            width: '100%',
            height: '100px'
          }}
        />
      );
  }
}

class Football extends React.Component {
  shoot() {
    alert("Great Shot!");
  }
  render() {
    return (
      <button onClick={this.shoot}>Take the shot!</button>
    );
  }
}

class DateComm extends React.Component {
  state = {
   dates: null
 }

 onSelect = dates => this.setState({dates})
  render() {

    return (
      <div>
      <DropdownButton id="dropdown-basic-button" title="Select Commodity">
        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
      </DropdownButton>
      <div id="dateBox">
      <DateRangePicker
         onSelect={this.onSelect}
         value={this.state.dates}
       />
       </div>

      </div>


    );
  }
}



document.body.style = 'background: lightblue;';


export default App;
