import React from 'react';
import { Route, Switch, withRouter } from 'react-router-dom';
import { Main, Search, Detail, Recommend } from './pages';
/**
 * @title Routes
 * @description Main Router
 */
const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={Main} />
      <Route exact path="/recommend/:genre/:movie1/:movie2/:movie3" component={Recommend} />
      <Route exact path="/search" component={Search} />
      <Route exact path="/:id" component={Detail} />
    </Switch>
  );
};

export default withRouter(Routes);
