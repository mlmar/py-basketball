import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/waiver')({
    component: RouteComponent
});

function RouteComponent() {
    return <div>Hello "/waiver"!</div>; // or improt whatever component here
}
