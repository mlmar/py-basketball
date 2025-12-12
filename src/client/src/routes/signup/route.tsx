import { Header } from '@/components/Header';
import { Section } from '@/components/Section';
import { Config } from '@/services/Config';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/signup')({
    component: RouteComponent
});

function RouteComponent() {
    return (
        <Section className='flex-col flex-fill flex-align-middle flex-justify-center'>
            <Header>
                <Header.Logo>WaiverWarrior</Header.Logo>
                <Header.Tagline>Sign Up for Fantasy Basketball Analytics</Header.Tagline>
            </Header>
            <form className='flex-col flex-fit' action={`${Config.SERVER_URL}/signup`} method='post'>
                <label className='flex-col'>
                    Username:
                    <input type='email' name='email' placeholder='Email' required />
                </label>
                <label className='flex-col'>
                    Password:
                    <input type='password' name='password' required />
                </label>
                <button type='submit'> Sign Up </button>
            </form>
        </Section>
    );
}
