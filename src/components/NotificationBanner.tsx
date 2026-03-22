import React, { useEffect, useState } from 'react';
import styles from './NotificationBanner.module.css';

const NotificationBanner: React.FC = () => {
  const [isScrolled, setIsScrolled] = useState<boolean>(false);

  // Detect scroll event to hide the banner
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 50) { // You can adjust the scroll value here
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };

    // Attach the scroll event listener
    window.addEventListener('scroll', handleScroll);

    // Cleanup the event listener when the component is unmounted
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    !isScrolled && (
      <div className={styles.banner}>
        <p>This is not the official MCP documentation. Created for <a style={{color: 'blue'}} href='https://www.youtube.com/@shantanukhond'>youtube.com/@shantanukhond</a></p>
      </div>
    )
  );
};

export default NotificationBanner;
