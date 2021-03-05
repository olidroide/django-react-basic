import React, { Component } from "react";
import { render } from "react-dom";
// import { observable, action } from "mobx";

// class PokemonModel {
//   @observable pokemons = [];

//   @action addPokemon(pokemon) {
//     this.pokemons.push({
//       id: uuid(),
//       ...pokemon,
//     });
//   }
// }

class ShowList extends React.Component {
  render() {
    return (
      <div>
        <h3> Leads </h3>
        <ul>
          {this.props.leads.map((lead) => {
            return (
              <li key={lead.id}>
                {lead.name} - {lead.email}
              </li>
            );
          })}
        </ul>
      </div>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/lead")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return <ShowList leads={this.state.data} />;
  }
}

export default App;
// export default PokemonModel;

const container = document.getElementById("app");
container ? render(<App />, container) : false;
