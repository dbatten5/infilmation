import React from 'react';
import Container from '@mui/material/Container';
import NavBar from './NavBar';

type Props = {
  children: React.ReactNode;
};

const Page = ({ children }: Props) => (
  <Container maxWidth="lg">
    <NavBar />
    {children}
  </Container>
);

export default Page;
