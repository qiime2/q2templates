import type { PageLoad } from './$types';

type Fetch = (input: RequestInfo | URL, init?: RequestInit) => Promise<Response>;

// If a report is this template, then we can use its children directly,
// otherwise, truncate the tree and use the report as a terminal viz
async function pruneIndex(node: Record<string, any>, fetch: Fetch) {
	for (const figure of Object.values(node)) {
		if (figure.children) {
			// check if this report is one of ourselves (or close enough)
			const ignoreCheck = [...figure.index.split('/').slice(0, -1), 'conf', 'collapse'].join('/');
			let response = await fetch(ignoreCheck);
			if (response.ok) {
				await pruneIndex(figure.children, fetch);
			} else {
				delete figure.children;
			}
		}
	}
}
export const load: PageLoad = async ({ fetch }) => {
	let result = await (await fetch('subfigures/index.json')).json();
	await pruneIndex(result, fetch);
	return result;
};
