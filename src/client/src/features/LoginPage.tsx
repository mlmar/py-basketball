import { Header } from '@/components/Header';
import { Section } from '@/components/Section';
import { Config } from '@/services/Config';

export function LoginPage() {
    return (
        <Section className='flex-col flex-fill flex-align-middle flex-justify-center'>
            <article className='flex-col gap'>
                <Header>
                    <Header.Logo>WaiverWarrior</Header.Logo>
                    <Header.Tagline>Fantasy Basketball Analytics</Header.Tagline>
                </Header>
                <form className='flex-col flex-fit form' action={`${Config.SERVER_URL}/login`} method='post'>
                    <label className='flex-col'>
                        email:
                        <input type='email' name='email' placeholder='Email' required />
                    </label>
                    <label className='flex-col'>
                        Password:
                        <input type='password' name='password' required />
                    </label>
                    <button className='btn primary' type='submit'>
                        Login
                    </button>
                </form>
            </article>
        </Section>
    );
}
