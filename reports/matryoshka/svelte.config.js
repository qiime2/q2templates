import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter(),
		// router filename will convert `index.html` to `index.html/` as it
		// really requires that the root of the router is at `/`, this is
		// independent of the trailingSlash options on the layout.
		router: { type: 'hash' },
		// without inline, it will generate rooted routes
		// `/_app/...` instead of `./_app/...`
		output: {
			bundleStrategy: 'inline'
		}
	}
};

export default config;
