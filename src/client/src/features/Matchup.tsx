import { Hero } from '@/components/Hero';

export function Matchup() {
    return (
        <Hero.Card>
            <h2>This Week's Matchup (Mock)</h2>
            <p className='matchup-label'>Overview</p>

            <div className='matchup-score'>
                <div>
                    <span className='matchup-name'>You</span>
                    <span className='matchup-record'>5–3</span>
                </div>
                <div>
                    <span className='matchup-name enemy'>Opponent</span>
                    <span className='matchup-record'>3–5</span>
                </div>
            </div>

            <p className='tiny-text'>
                Target categories: <strong>FG%</strong>, <strong>AST</strong>, <strong>3PM</strong>,<strong>STL</strong>
                .
            </p>
        </Hero.Card>
    );
}
