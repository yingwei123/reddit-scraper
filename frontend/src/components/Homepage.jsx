import {React, useState } from 'react';
import {Button,Grid, TextField} from '@mui/material';
import '../style/home_page.css';
import Footer from './Footer';
import {getRequest} from '../utils/api'
import { useNavigate  } from 'react-router-dom';

const HomePage = ({setRowData}) =>{
    const navigate = useNavigate();
    const [redditPostURL, setRedditPostURL] = useState("")
    const [errorMessage, setErrorMessage] = useState("")

    const goToLink = (path) => {
        navigate(path);
    };

    const handleScrape = async() =>{
        const regexPattern = /^https:\/\/www\.reddit\.com\/r\/[^/]+\/comments\/[^/]+\/[^/]+\/?$/;

        if(!regexPattern.test(redditPostURL)){
            setErrorMessage("Expected a link of this format: https:www.reddit.com/r/*/comments/*/* where * can be any value")
            return
        }

        setErrorMessage("")

        try{
            const data = await getRequest("/reddit-data",{"reddit_url":redditPostURL})
            setRowData(data)
            goToLink("/table")
        }catch(error){
            setErrorMessage("Failed to get request, please try again later")
        }
     
    }

    const handleOnChange = (event) =>{
        setRedditPostURL(event.target.value);
    }

    return(
        <>
            <Grid item className = "home-page" xs= {12}>
                <Grid item>
                    <Grid item xs = {12}>
                        <TextField id="outlined-basic" label="Reddit Post URL" variant="outlined" onChange={handleOnChange} className="input-link"/>
                    </Grid>
                    <Grid item>
                        <Button onClick={handleScrape} className='top-margin'>Scrape Data</Button>
                    </Grid>
                    <Grid className='top-margin error-message'>
                        {errorMessage}
                    </Grid>
                </Grid>  
            </Grid>
            <Footer/>
        
        </>
    )
}

export default HomePage