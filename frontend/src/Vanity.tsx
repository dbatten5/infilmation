import React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Avatar from '@mui/material/Avatar';
import useMediaQuery from '@mui/material/useMediaQuery';
import { useTheme } from '@mui/material/styles';
import Link from '@mui/material/Link';

const Vanity = () => {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up('xl'));

  return (
    <Box
      sx={{
        position: 'fixed',
        right: { xs: '0.5rem', sm: '1rem', xl: '2rem' },
        bottom: { xs: '0.5rem', sm: '1rem', xl: '2rem' },
      }}
    >
      <Stack
        direction={matches ? 'row' : 'column'}
        alignItems="center"
        spacing={1.5}
      >
        <Link
          href="https://github.com/dbatten5"
          target="_blank"
          sx={{ '&:hover': { opacity: 0.6, transition: '0.3s' } }}
        >
          <Avatar
            alt="GitHub Logo"
            src="./github-64.png"
            sx={{
              width: { xs: '1rem', md: '1.2rem' },
              height: { xs: '1rem', md: '1.2rem' },
            }}
          />
        </Link>
        {/* <Link */}
        {/*   href="https://www.linkedin.com/in/dominic-batten-669996a0/" */}
        {/*   target="_blank" */}
        {/*   sx={{ '&:hover': { opacity: 0.6, transition: '0.3s' } }} */}
        {/* > */}
        {/*   <Avatar */}
        {/*     alt="LinkedIn Logo" */}
        {/*     src="./linkedin-64.png" */}
        {/*     sx={{ */}
        {/*       width: { xs: '1rem', md: '1.2rem' }, */}
        {/*       height: { xs: '1rem', md: '1.2rem' }, */}
        {/*     }} */}
        {/*   /> */}
        {/* </Link> */}
      </Stack>
    </Box>
  );
};

export default Vanity;
