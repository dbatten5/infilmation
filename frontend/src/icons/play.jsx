import * as React from 'react';

function SvgComponent(props) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" height={20} width={20} {...props}>
      <path fill="none" d="M0 0h24v24H0z" />
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-2.5-3.5l7-4.5-7-4.5v9z" />
    </svg>
  );
}

export default SvgComponent;
