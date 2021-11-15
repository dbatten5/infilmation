import React from 'react';
import Container from '@mui/material/Container';
import NavBar from './NavBar';
import BackgroundCanvas from './BackgroundCanvas';

type Props = {
  children: React.ReactNode;
};

const Page = ({ children }: Props) => (
  <>
    <BackgroundCanvas />
    <Container
      maxWidth="lg"
      sx={{ px: { xs: '2rem', sm: '3rem', zIndex: 1 } }}
      disableGutters
    >
      <NavBar />
      {children}
    </Container>
  </>
);

export default Page;
