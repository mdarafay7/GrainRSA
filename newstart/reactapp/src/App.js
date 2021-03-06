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
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";
import moment from "moment";





class App extends Component {
shoot()
{
  ReactDOM.render(<DateComm/>, document.getElementById('root'));

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



class DateComm extends React.Component {



constructor(props)
{
  super();
  this.state={
    startDate: new Date(),
    endDate: new Date(),
    datex: "AS",
    commodity:'none',
    startDatetoggle:false,
    endDatetoggle:false

  };
}


handleChange1(date) {

  var dates=moment(date).format('YYYY-MM-DD');
  this.setState({startDate: dates});
  this.setState({startDatetoggle: true});


};

handleChange2(date) {

  var dates=moment(date).format('YYYY-MM-DD');
  this.setState({endDate: dates});
  this.setState({endDatetoggle: true});


};
setComm(comm_type) {

  this.setState({commodity: comm_type});

};



 print(comm,date,date2){
   console.log(date);
   if(!this.state.endDatetoggle)
   {
     ReactDOM.render(<Select comm={this.state.commodity} date={date} date2={"none"}/>, document.getElementById('root'));

   }
   else{
   ReactDOM.render(<Select comm={this.state.commodity} date={date} date2={date2}/>, document.getElementById('root'));
}
 }

  render() {

    return (
      <div>
      <DropdownButton id="dropdown-basic-button" title="Select Commodity">
        <Dropdown.Item onClick={() => this.setComm("YM")}>YM</Dropdown.Item>
        <Dropdown.Item onClick={() => this.setComm("WM")}>WM</Dropdown.Item>
        <Dropdown.Item onClick={() => this.setComm("SUN")}>Something else</Dropdown.Item>
      </DropdownButton>
      <div id="dateBox">
      <DatePicker
  selected={this.state.date}
  onSelect={this.handleSelect} //when day is clicked
  onChange={startDate => this.handleChange1(startDate)}
  />
  <DatePicker
selected={this.state.date}
onSelect={this.handleSelect} //when day is clicked
onChange={endDate => this.handleChange2(endDate)}
/>
       </div>


       <button onClick={() => { this.print("YM",this.state.startDate,this.state.endDate)}}>ClickME</button>

      </div>

    );
  }


}

class Select extends React.Component {
constructor(){
  super();
  this.state={
    information: [],
  };
}



  componentDidMount(){
    this.getInformation();

  }
  getInformation= _ =>{
    if(this.props.date2=="none")
    {
      console.log(this.props.val);
        fetch('http://localhost:4000/select_date?date='+this.props.date+"&comm="+this.props.comm)
          .then(response=>response.json())
          .then(response=>this.setState({information: response.data}))
          .catch(err=>console.error(err))
    }
    else{
    console.log(this.props.val);
      fetch('http://localhost:4000/select_range?date='+this.props.date+"&comm="+this.props.comm+"&date2="+this.props.date2)
        .then(response=>response.json())
        .then(response=>this.setState({information: response.data}))
        .catch(err=>console.error(err))
      }
  }





  renderInformation=({DATE,ID,COMMODITY,SETTLEMENT,HIGH,LOW,VOL,OPEN_INT})=><div key={DATE}>{ID}>{COMMODITY}>{SETTLEMENT}>{HIGH}>{LOW}>{VOL}>{OPEN_INT}</div>
  render(){
    const {information}=this.state;
    return(


      <div className="container">

              <div className="panel panel-default p50 uth-panel">
                  <table className="table table-hover">
                      <thead>
                          <tr>
                              <th>Date</th>
                              <th>ID</th>
                              <th>Commodity</th>
                              <th>Settlement</th>
                              <th>High</th>
                              <th>Low</th>
                              <th>Vol</th>
                              <th>OPEN_INT</th>
                          </tr>
                      </thead>
                      <tbody>
                      {this.state.information.map(renderInformation=>
                          <tr key={renderInformation.id}>
                          <td>{renderInformation.DATE} </td>
                          <td>{renderInformation.ID}</td>
                          <td>{renderInformation.COMMODITY}</td>
                          <td>{renderInformation.SETTLEMENT}</td>
                          <td>{renderInformation.HIGH}</td>
                          <td>{renderInformation.LOW}</td>
                          <td>{renderInformation.VOL}</td>
                          <td>{renderInformation.OPEN_INT}</td>
                          </tr>
                      )}
                      </tbody>
                  </table>

              </div>

          </div>
    );
  }
}




document.body.style = 'background: lightblue;';


export default App;
