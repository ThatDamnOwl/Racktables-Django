import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";

class New$MODELNAME$Form extends React.Component {
    state = {
        $FIELDSWITHDEFAULTS$
    };

    componentDidMount() {
        if (this.props.$MODELNAME$) {
            const { $FIELDS$ } = this.props.$MODELNAME$
            this.setState({ $FIELDS$ });
        }
    }

    onChange = edit => {
        this.setState({[edit.target.name]: edit.target.value});
    }

    create$MODELNAME$ = edit => {
        edit.preventDefault();

        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    }

    edit$MODELNAME$ = edit => {
        e.preventDefault()
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    }

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    }

  render() {
    return (
      <Form onSubmit={this.props.$MODELNAME$ ? this.edit$MODELNAME$ : this.create$MODELNAME$}>
        $FORMFIELDS$
        <Button>Send</Button>
      </Form>
    );
}

export default Header;