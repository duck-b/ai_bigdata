import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { Main, User } from './pages';
/**
 * @title Routes
 * @description Main Router
 */
const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={Main} />
      <Route path="/user" component={User} />
    </Switch>
  );
};

export default Routes;
