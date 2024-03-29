import * as React from 'react';

function Rt(props) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlnsXlink="http://www.w3.org/1999/xlink"
      width={25}
      height={25}
      viewBox="0 0 80 80"
      {...props}
    >
      <defs>
        <path id="prefix__a" d="M0 .247h77.083v63.468H0z" />
      </defs>
      <g fill="none" fillRule="evenodd">
        <g transform="translate(1.328 16.266)">
          <mask id="prefix__b" fill="#fff">
            <use xlinkHref="#prefix__a" />
          </mask>
          <path
            d="M77.014 27.043C76.242 14.674 69.952 5.42 60.488.247c.053.301-.215.678-.52.545-6.19-2.708-16.693 6.056-24.031 1.466.055 1.647-.267 9.682-11.585 10.148-.268.011-.415-.262-.246-.455 1.514-1.726 3.042-6.097.845-8.428-4.706 4.217-7.44 5.804-16.463 3.71C2.711 13.274-.562 21.542.08 31.841c1.311 21.025 21.005 33.044 40.837 31.806 19.83-1.236 37.408-15.58 36.097-36.604"
            fill="#FA320A"
            mask="url(#prefix__b)"
          />
        </g>
        <path
          d="M42.2 11.465c4.075-.971 15.796-.095 19.551 4.887.225.299-.092.864-.455.705-6.19-2.708-16.693 6.056-24.032 1.467.056 1.647-.266 9.682-11.585 10.148-.267.01-.414-.262-.245-.455 1.514-1.727 3.042-6.098.845-8.428-5.127 4.594-7.906 6.07-19.032 3.062-.364-.098-.24-.683.147-.83 2.103-.804 6.867-4.324 11.374-5.876a15.308 15.308 0 012.549-.657c-4.963-.444-7.2-1.134-10.356-.658a.392.392 0 01-.367-.627c4.253-5.478 12.088-7.132 16.922-4.222-2.98-3.692-5.314-6.636-5.314-6.636l5.53-3.142 3.948 8.82c4.114-6.078 11.768-6.639 15.001-2.326.192.256-.008.62-.328.613-2.633-.064-4.082 2.33-4.192 4.15l.039.005"
          fill="#00912D"
        />
      </g>
    </svg>
  );
}

export default Rt;
