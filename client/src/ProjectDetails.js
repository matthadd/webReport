import React, {Component} from 'react';
import Panel from 'react-bootstrap/lib/Panel'
import axios from 'axios'

//This Component is a child Component of Projects Component
export default class ProjectDetails extends Component {

  constructor(props) {
    super(props);
    this.state = {}
  }

  //Function which is called when the component loads for the first time
  componentDidMount() {
    this.getProjectDetails(this.props.val)
  }

  //Function which is called whenver the component is updated
  componentDidUpdate(prevProps) {

    //get Project Details only if props has changed
    if (this.props.val !== prevProps.val) {
      this.getProjectDetails(this.props.val)
    }
  }

  //Function to Load the projectdetails data from json.
  getProjectDetails(id) {
    axios.get('assets/samplejson/project' + id + '.json').then(response => {
      this.setState({projectDetails: response})
    })
  };

  render() {
    if (!this.state.projectDetails)
      return (<p>Loading Data</p>)
    return (<div className="projectdetails">
      <Panel bsStyle="info" className="centeralign">
        <Panel.Heading>
          <Panel.Title componentClass="h3">{this.state.projectDetails.data.name}</Panel.Title>
        </Panel.Heading>
        <Panel.Body>
          <p>Name : {this.state.projectDetails.data.name}</p>
          <p>Email : {this.state.projectDetails.data.project_manager}</p>
          <p>Phone : {this.state.projectDetails.data.phone}</p>
          <p>City : {this.state.projectDetails.data.city}</p>
          <p>State : {this.state.projectDetails.data.state}</p>
          <p>Country : {this.state.projectDetails.data.country}</p>
          <p>Organization : {this.state.projectDetails.data.organization}</p>
          <p>Job Profile : {this.state.projectDetails.data.jobProfile}</p>
          <p>Additional Info : {this.state.projectDetails.data.additionalInfo}</p>
        </Panel.Body>
      </Panel>
    </div>)
  }
}
