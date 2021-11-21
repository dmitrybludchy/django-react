import React from 'react'
import { Container } from 'react-bootstrap'
import { BrowserRouter as Router, Route } from "react-router-dom"
import './bootstrap.min.css'
import Footer from './components/Footer'
import Header from './components/Header'
import CartScreen from './screens/CartScreen'
import HomeScreen from './screens/HomeScreen'
import LoginScreen from './screens/LoginScreen'
import RegisterScreen from './screens/RegisterScreen'
import ProductScreen from './screens/ProductScreen'

function App() {
  return (
    <Router>
      <Header />
      <main className="p-3">
        <Container>
          <Route path='/' component={HomeScreen} exact />
          <Route path='/login' component={LoginScreen} />
          <Route path='/register' component={RegisterScreen} />
          <Route path='/product/:id' component={ProductScreen} />
          <Route path='/cart/:id?' component={CartScreen} />
        </Container>
      </main>
      <Footer />
    </Router>

  );
}

export default App
