import React from 'react';
import Container from '@mui/material/Container';
import NavBar from './NavBar';

type Props = {
  children: React.ReactNode;
};

const Page = ({ children }: Props) => (
  <Container
    maxWidth="lg"
    sx={{ px: { xs: '2rem', sm: '3rem' } }}
    disableGutters
  >
    <NavBar />
    {children}
  </Container>
);

export default Page;
